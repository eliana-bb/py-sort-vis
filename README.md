# py-sort-vis
Python sort visualizer, outputs PNGs.

imgout.sortImage(array, name) is a method that saves a PNG to ./imgs (subfolder in the working directory).
It takes a list of ints [0..n] whose length is equal to n+1 (e.g. [0,1,2,3]) and renders it in a 1080p PNG, saved to ./imgs/[name].png

huergb.hue(int) is a method that takes a value (0,1529) and returns the appropriate RGB-hue (at 100 brightness and saturation) in the form of a tuple (R, G, B). Note that unlike conventional hue (0,359), huergb scales much slower.
