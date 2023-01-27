def solution(files):
    temp_answer = []
    answer = []
    for file_index in range(len(files)):
        temp_list = [files[file_index]] + [""] * 3
        start = 1
        temp_index = 0
        for i in range(temp_index, len(files[file_index])):
            if files[file_index][i].isdigit():
                start += 1
                temp_index = i
                break
            temp_list[start] += files[file_index][i]
            print(i)
        for i in range(temp_index, len(files[file_index])):
            if not files[file_index][i].isdigit():
                start += 1
                temp_index = i
                break
            temp_list[start] += files[file_index][i]
            print(i)
        for i in range(temp_index, len(files[file_index])):
            # if files[file_index][i].isdigit():
            #     start += 1
            #     temp_index = i
            #     break
            print(i)
            temp_list[start] += files[file_index][i]
            
        temp_list.append(temp_list[1].lower())
        temp_list.append(int(temp_list[2]))
        temp_list.append(file_index)
        temp_answer.append(temp_list)
    print(temp_answer)
    temp_answer.sort(key = lambda x : (x[4], x[5], x[6]))
        
    
    for name in temp_answer:
        answer.append(name[0])
    return answer

print(solution( ["O00321"]))
# print(solution( ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]) == ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"])
# print(solution( ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
