class Solution:
    def myAtoi(self, s: str) -> int:
        accept=['-','+',' ','0','1','2','3','4','5','6','7','8','9']
        temp_list=[]
        sign=True
        floor='-2147483648'
        ceil= '2147483647'
        removal=['+','-',' ']
        nonsense=['-+','--','- ','++','+-','+ ','0+','0-','0 ']
        last=""
        for char in s:
            if char in accept:
                if char=='-' and last.isdigit()==False:
                    temp_list+=[char]
                    last=char
                    sign=False
                elif char=='+'or char==' ':
                    if char in removal and last.isdigit():
                        break
                    else:
                        temp_list+=[char]
                        last=char
                        continue
                else:
                    temp_list+=[char]
                    last=char
            else:
                break
        temp_list=''.join(temp_list)

        if len(temp_list)==0:
            return 0
        if any(char.isdigit() for char in temp_list)==False:
            return 0
        for n in nonsense:
            if n in temp_list:
                return 0
        for r in removal:
            temp_list=temp_list.replace(r,"")
        
        temp_list=str(int(temp_list))      
        if len(temp_list)==10:
            if sign:
                if int(ceil)-int(temp_list) >=0:
                   return int(temp_list)
                else:
                    return int(ceil)
            else:
                if int(floor) + int(temp_list) <=0:
                   return int(temp_list)*-1
                else:
                    return int(floor)
        elif len (temp_list)>10:
            if sign:
                return int(ceil)
            else:
                return int(floor)
        elif sign:
            return int(temp_list)
        else:
            return int(temp_list)*-1


# sol=Solution()
# string="-2147483647"
# print(sol.myAtoi(string))
            