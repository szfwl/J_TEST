
def test(name,pwd):
    print(name)
    print(pwd)

if __name__ == "__main__":
    info = ("name","123")

    test(*info)