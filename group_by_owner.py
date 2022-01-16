def group_by_owner(input_dict):
    output_dict={}
    for i in input_dict:
        if input_dict[i] in output_dict: # Checks if the owner is already present in the ouput dictionary
            output_dict[input_dict[i]].append(i)
        else:
            list1=[i]
            output_dict[input_dict[i]]=list1

    return output_dict

if __name__=="__main__":
    input=eval(input())
    print(group_by_owner(input))