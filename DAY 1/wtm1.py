# Testing r+ and w+

fb = open("test.txt", "w+")
print(fb.name)
print(fb.mode)
fb.write("Hi!!");
kem = fb.read();
print(kem)
fb.close()