// Render lines of text with Core Text (the macOS text engine Safari and TextEdit use) to a PNG, and
// print the glyphs Core Text chose for each line. Used by tools/font_gate.py --coretext.
//   swift ctrender.swift FONTFILE LINESFILE OUT.png
// LINESFILE: one "label<TAB>text" per row. The font is loaded from the file, not by installed name.
import CoreGraphics
import CoreText
import Foundation
import ImageIO
import UniformTypeIdentifiers

let args = CommandLine.arguments
guard args.count == 4 else { print("usage: ctrender FONT LINES OUT.png"); exit(2) }
let fontURL = URL(fileURLWithPath: args[1]) as CFURL
guard let descs = CTFontManagerCreateFontDescriptorsFromURL(fontURL) as? [CTFontDescriptor], let desc = descs.first else {
    print("could not load font"); exit(1)
}
let font = CTFontCreateWithFontDescriptor(desc, 72, nil)
print("font:", CTFontCopyFullName(font))
let lines = try! String(contentsOfFile: args[2], encoding: .utf8).split(separator: "\n").map(String.init)

let rowH: CGFloat = 130, width: CGFloat = 900
let height = rowH * CGFloat(lines.count) + 20
let ctx = CGContext(data: nil, width: Int(width), height: Int(height), bitsPerComponent: 8, bytesPerRow: 0,
                    space: CGColorSpaceCreateDeviceRGB(), bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue)!
ctx.setFillColor(CGColor(red: 1, green: 1, blue: 1, alpha: 1))
ctx.fill(CGRect(x: 0, y: 0, width: width, height: height))
let label = CTFontCreateWithName("Helvetica" as CFString, 14, nil)
for (i, text) in lines.enumerated() {
    let parts = text.components(separatedBy: "\t")  // "label<TAB>tengwar"
    let y = height - rowH * CGFloat(i + 1)
    let black = CGColor(red: 0, green: 0, blue: 0, alpha: 1)
    if parts.count == 2 {
        let l = CTLineCreateWithAttributedString(NSAttributedString(string: parts[0], attributes: [
            NSAttributedString.Key(kCTFontAttributeName as String): label,
            NSAttributedString.Key(kCTForegroundColorAttributeName as String): black]))
        ctx.textPosition = CGPoint(x: 20, y: y + 50); CTLineDraw(l, ctx)
    }
    let tw = CTLineCreateWithAttributedString(NSAttributedString(string: parts.last!, attributes: [
        NSAttributedString.Key(kCTFontAttributeName as String): font,
        NSAttributedString.Key(kCTForegroundColorAttributeName as String): black]))
    ctx.textPosition = CGPoint(x: 560, y: y + 35); CTLineDraw(tw, ctx)
    // Report the glyphs Core Text chose, so substitutions (e.g. shifted tehtar) are visible as data.
    let runs = CTLineGetGlyphRuns(tw) as! [CTRun]
    var names: [String] = []
    for run in runs {
        let n = CTRunGetGlyphCount(run)
        var glyphs = [CGGlyph](repeating: 0, count: n)
        CTRunGetGlyphs(run, CFRange(location: 0, length: n), &glyphs)
        let runFont = (CTRunGetAttributes(run) as NSDictionary)[kCTFontAttributeName as String] as! CTFont
        for g in glyphs { names.append((CTFontCopyNameForGlyph(runFont, g) as String?) ?? "#\(g)") }
    }
    print("\(parts.first!): \(names.joined(separator: " "))")
}
let dest = CGImageDestinationCreateWithURL(URL(fileURLWithPath: args[3]) as CFURL, UTType.png.identifier as CFString, 1, nil)!
CGImageDestinationAddImage(dest, ctx.makeImage()!, nil)
CGImageDestinationFinalize(dest)
