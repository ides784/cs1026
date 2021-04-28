from volume import cubevol, ellipsoidvol, pyramidvol
mylist = []

while True:
    shape = input("Please enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e): ")
    if shape.lower() == "pyramid" or shape.lower() == "p":
        b = float(input("Enter the base of the pyramid: "))
        h = float(input("Enter the height of the pyramid: "))
        print("The volume of a pyramid with base {:.1f} and height {:.1f} is: {:.2f}\n".format(b, h, pyramidvol(b, h)))
        mylist.append(("pyramid", (pyramidvol(b, h))))
    elif shape.lower() == "cube" or shape.lower() == "c":
        a = float(input("Enter length of side for the cube: "))
        print("The volume of a cube with side {:.1f} is: {:.2f}\n".format(a, cubevol(a)))
        mylist.append(("cube", (cubevol(a))))
    elif shape.lower() == "ellipsoid" or shape.lower() == "e":
        r1 = float(input("Enter the first radius: "))
        r2 = float(input("Enter the second radius: "))
        r3 = float(input("Enter the third radius: "))
        print("The volume of an ellipsoid with radii {:.1f} and {:.1f} and {:.1f} is: {:.2f}\n".format(r1, r2, r3, ellipsoidvol(r1, r2, r3)))
        mylist.append(("ellipsoid", (ellipsoidvol(r1, r2, r3))))
    elif shape.lower() == "quit" or shape.lower() == "q":
        break
    else:
        print("error, please input a shape")

if not mylist:
    print("No shapes entered.")
else:
    mylist.sort(key=lambda mylist: mylist[1])
    print("Output: Volumes of shapes entered in sorted order: ")
    for shape, vol in mylist:
        rounded = '{:.2f}'.format(vol)
        print(shape, rounded)


