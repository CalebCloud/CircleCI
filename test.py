from app import Add

def TestAdd():
        assert Add(2,3) == 5
        print("Add Function works correctly")

if __name__ == '__app__':
        TestAdd()