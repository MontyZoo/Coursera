//: Playground - noun: a place where people can play

import UIKit


func increase(input: Int, delta: Int) -> UInt32 {
    var ret = input + delta
    if ret > 255
    {
        ret = 255
    }
    return UInt32(ret)
}

let image = UIImage(named: "sample")

let myRGBA = RGBAImage(image: image!)!

var totalRed = 0
var totalGreen = 0
var totalBlue = 0

for y in 0..<myRGBA.height {
    for x in 0..<myRGBA.width {
        let index = y * myRGBA.width
        var pixel = myRGBA.pixels[index]
        //totalRed += Int(pixel.red)
        //totalGreen += Int(pixel.green)
        //totalBlue += Int(pixel.blue)
        pixel.red = increase(Int(pixel.red), delta:30)
        pixel.green = increase(Int(pixel.green), delta:30)
        pixel.blue = increase(Int(pixel.blue), delta:30)
    }
}

// Gaussian Blur Filter

// Solarizing Filter

// Find Edges Filter

// Glowing Edges Filter

// Embossing Filter

// http://www.pcmag.com/encyclopedia/term/44794/image-filter
