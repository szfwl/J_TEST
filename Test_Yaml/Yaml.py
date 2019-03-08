
import yaml

with open("./data.yml","r",encoding='utf-8') as f:
    data = yaml.load(f)
    # print(type(data))
    # print(data)

    # print(data.get("qweee"))
    testdata = data.get("Test")
    print(testdata)
    for list in testdata.keys():
        # print("test: %s \n test_name: %s \n test_pwd: %s \n"
        #       %(list,testdata.get(list).get("name"),testdata.get(list)
        #         .get("pwd")))

        print("test: %s \n test_pwd: %s \n test_name: %s \n"
              %(list,testdata.get(list).get("pwd"),testdata.get(list).get("name")))