def main():
 argv=[]
 count=len(argv)
 print("{} arguments:".format(count))

 argv.append(input("enter argument: "))
 count=len(argv)
 print("{} argument.".format(count))
 print("{}: {}".format(count, argv[0]))

 argv.append(input("enter argument: "))
 count=len(argv)
 print("{} arguments:".format(count))
 print("{}: {}".format(count-1, argv[0]))
 print("{}: {}".format(count, argv[1]))



 argv.append(input("enter argument: "))
 count=len(argv)
 print("{} arguments:".format(count))
 print("{}: {}".format(count-2, argv[0]))
 print("{}: {}".format(count-1, argv[1]))
 print("{}: {}".format(count, argv[2]))


 argv.append(input("enter argument: "))
 count=len(argv)
 print("{} arguments:".format(count))
 print("{}: {}".format(count-3, argv[0]))
 print("{}: {}".format(count-2, argv[1]))
 print("{}: {}".format(count-1, argv[2]))
 print("{}: {}".format(count, argv[3]))


 argv.append(input("enter argument: "))
 count=len(argv)
 print("{} arguments:".format(count))
 print("{}: {}".format(count-4, argv[0]))
 print("{}: {}".format(count-3, argv[1]))
 print("{}: {}".format(count-2, argv[2]))
 print("{}: {}".format(count-1, argv[3]))
 print("{}: {}".format(count, argv[4]))


 argv.append(input("enter argument: "))
 count=len(argv)
 print("{} arguments:".format(count))
 print("{}: {}".format(count-5, argv[0]))
 print("{}: {}".format(count-4, argv[1]))
 print("{}: {}".format(count-3, argv[2]))
 print("{}: {}".format(count-2, argv[3]))
 print("{}: {}".format(count-1, argv[4]))
 print("{}: {}".format(count, argv[5]))
if __name__ =="__main__":
   main()
print(main())


























"""for i in range(1,7):
    print("{}: {}".format(count,element))
    element=input("enter the element: ")
    argv.append(element)
    count=len(argv)
    print("{} arguments:".format(count))
    print("{}: {}".format(count,element))"""