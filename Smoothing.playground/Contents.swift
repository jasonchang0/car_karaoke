//: Playground - noun: a place where people can play

import UIKit

extension Array {
    // the mutating function should be named "filter" but
    // this is already taken by the non-mutating function
    mutating func filtering(_ isIncluded: (Element) throws -> Bool) rethrows -> [Element] {
        try self = self.filter(isIncluded)
        return self
    }
}

func simple_smooth(_ frequency: [Double]) -> [Double] {
    var smooth_freq = [Double]()
    for i in 0...frequency.count-1 {
        if 1 <= i && i <= frequency.count-2 {
            smooth_freq += [(frequency[i - 1] + frequency[i] + frequency[i + 1])/3]
            continue
        }
        
        smooth_freq += [frequency[i]]
    }

    return smooth_freq
}

func triangular_smooth(_ frequency: [Double]) -> [Double] {
    var smooth_freq = [Double]()
    
    for i in 0...frequency.count-1 {
        if 2 <= i && i <= frequency.count-3 {
            smooth_freq += [(frequency[i - 2] + 2 * frequency[i - 1] + 3 * frequency[i] + 2 * frequency[i + 1] + frequency[i + 2])/9]
            continue
        }
        
        smooth_freq += [frequency[i]]
    }
    
    return smooth_freq
}

var sample_freq = [0.3246444940270937, 0.45477269317766844, 0.09002986011353986, 0.6272121860071521, 0.5894602337658823, 0.2497897317701091, 0.15088883790657204, 0.015120828522128149, 0.8985269636656094, 0.660054893817381]

print(simple_smooth(sample_freq))

print(triangular_smooth(sample_freq))







