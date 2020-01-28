import xml.etree.ElementTree as ET
from ClassDataStruct import *

def main():

    # tree = ET.parse('web.xml')
    tree = ET.parse('applicationContext.xml')

    root = tree.getroot()

    # print("root.tag:" + root.tag)
    # print("root.attribute:")
    # print(root.attrib)
    #
    # print("")

    singleton_class_list = []
    singleton_class_name_list = []

    for child in root:
        # print("child.tag:" + child.tag)
        # print("child.attrib:")
        # print(child.attrib)
        #
        # print(child.attrib["id"])
        # print(child.attrib["class"])

        child_id = child.attrib["id"]

        if not child_id:
            # empty
            print("child_id is empty")
            pass
        else:

            child_class = child.attrib["class"]

            if not child_class:
                # empty
                print("child_class is empty")
                pass
            else:

                class_path_name = child_class + ".java"
                class_name_list = child_class.split('.')
                class_name = class_name_list[-1] + ".java"

                singleton_bean_class = SingletonBeanClass(class_name, class_path_name)

                singleton_class_list.append(singleton_bean_class)

                singleton_class_name_list.append(class_name)

        # #print(child.attrib.id)
        # #print(child.attrib.class)
        #
        # print("")

    print("-------------")

    for clsdss_data in singleton_class_list:
        print(clsdss_data.class_name)
        print(clsdss_data.class_path_name)
        print("")

    print("-------------")


    search_flg = "WcGetIdStlMngNoServiceImpl.java" in singleton_class_name_list
    print(search_flg)


# プログラムのエントリポイント
if __name__ == "__main__":

    # メイン処理
    main()

