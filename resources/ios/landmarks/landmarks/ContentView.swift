//
//  ContentView.swift
//  landmarks
//
//  Created by Gloria Ju on 2022/11/26.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack(alignment: .trailing) {
            Image(systemName: "globe")
                .imageScale(.medium)
                .foregroundColor(.accentColor)
            Text("Hello, swiftUI!")
        }
        .padding()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
