# soru = [1, 4, 8, [3, 6, [5, 67, 34], 11], [14, 16], 25]
# answer = [1, 3, 4, 5, 6, 8, 11, 14, 16, 25, 34, 67]

num = [1, 4, 8, [3, 6, [5, 67, 34], 11], [14, 16], 25]
ans = []
for i in num:
    if type(i) == list:
        for j in i:
            if type(j) == list:
                for k in j:
                    ans.append(k)
            else:
                ans.append(j)
    else:
        ans.append(i)
print(sorted(ans))


#solution 2-3
# lst=[[5,7, [3,4,[12]],[6],[1,2],9],[1,2,[11]], [[[[[9]]]]]]
# lst2=[]
# # for i in lst:
# #     if not isinstance(i, list):
# #         lst2.append(i)
# #         continue
# #     for j in i:
# #         if not isinstance(j, list):
# #             lst2.append(j)
# #             continue
# #         for k in j:
# #             if not isinstance(k,list):
# #                 lst2.append(k)
# #                 continue
# #             for z in k:
# #                 lst2.append(z) 
# # print(lst2)
# def lst_cont(a):
#     for i in a:
#         if not isinstance(i, list):
#             lst2.append(i)
#             continue
#         lst_cont(i)  
# lst_cont(lst) 
# print(sorted(lst2))