
#bai 4.3
alien_color=['green','yellow','red']
diem=0
for i in range (len(alien_color)):
    if alien_color[i]=='green':
       diem+=5
       print("nguoi choi kiem duoc 5 diem")
      
for i in range (len(alien_color)):
    if alien_color[i]!='green':
       continue  
#bai 4.4
rs=0
alien_color=['green', 'yellow', 'red', 'blue','black']
for i in range(len(alien_color)):
    if alien_color[i]=='green':
        rs+=5
    else : rs+=10
#bai 4.5
alien_color=['green', 'yellow', 'red']
for i in range(len(alien_color)):
    if alien_color[i]=='green':
        rs+=5
        print("nguoi choi duoc 5")
    elif alien_color[i]=='yellow':
        rs+=10
        print("nguoi choi duoc 10")
    else: 
        rs+=15
        print("nguoi choi duoc 15")
#bai4.6
age=50
if age<2 : print("baby")
elif age>=2 and age<4 : print("toddler")
elif age >=4 and age<13: print("kid")
elif age >=13 and age<20: print("teenager")
elif age >=20 and age<65 : print("adult")
elif age>=65: print("elder")
#bai 4.7
ds1=['apple','tomato','eeg','watermallon']
favorite_fruits=['apple', 'bananna','orange']
ok=1
for i in ds1:
    if  i in favorite_fruits :
        ok =0
if ok==0 : print("You really like bananas!")
#bai4.8
ad_min=['ngoc','phuong', 'du', 'quan tri vien']
for i in range (len(ad_min)):
    if ad_min[i]=='quan tri vien':
        print("Xin chao ",ad_min[i],", ban co muon xem bao cao trang thai khong")
    else :print("xin chao ",ad_min[i],", cam on vi dang nhap lai")
#bai 4.9   
ok1=1
for i in range (len(ad_min)):
    if ad_min[i]=='quan tri vien':
        print("Xin chao ",ad_min[i],", ban co muon xem bao cao trang thai khong")
    else :
        ok1=0
        ad_min.pop(i)
if ok1==1 : print(" We need to find some users!")
#bai 4.10
current_user=['PHUong', 'Ngoc', 'dU', 'DUong']
for i in range(len(current_user)):
    current_user[i]=current_user[i].lower
new_user=['phuong', 'DU']    
for i in range(len(new_user)):
    new_user[i]=new_user[i].lower
for i in new_user:
    if i in current_user:
        print("can nhap ten nguoi dung moi")
    else: print("ten nguoi dung kha dung")
#bai 4.11
Ordinal_Numbers =[1,2,3,4,5,6,7,8,9]
Ordinal_Numbers.sort
dem=1
s=""
for i in range(len(Ordinal_Numbers)-1):
       
        if (Ordinal_Numbers[i]==Ordinal_Numbers[i+1]):
            dem+=1
        elif i==len(Ordinal_Numbers)-1 and Ordinal_Numbers[i] ==Ordinal_Numbers[i+1]:
            dem+=1
        else:
            dem=1
            if Ordinal_Numbers[i]==1:
               s=s+str(Ordinal_Numbers[i])+"st"
            elif Ordinal_Numbers[i]==2:
                   s=s+str(Ordinal_Numbers[i])+"nd"
            elif Ordinal_Numbers[i]==3:
                   s=s+str(Ordinal_Numbers[i])+"rd"
            else:
                s=s+str(Ordinal_Numbers[i])+"th"
if Ordinal_Numbers(len(Ordinal_Numbers)-1)==1:
    s=s+str(Ordinal_Numbers(len(Ordinal_Numbers)-1))+"st"
elif Ordinal_Numbers(len(Ordinal_Numbers)-1)==2:
    s=s+str(Ordinal_Numbers(len(Ordinal_Numbers)-1))+"nd"
elif Ordinal_Numbers(len(Ordinal_Numbers)-1)==3:
    s=s+str(Ordinal_Numbers(len(Ordinal_Numbers)-1))+"rd"
else :s=s+str(Ordinal_Numbers[i])+"th"
print(s)
       
             
