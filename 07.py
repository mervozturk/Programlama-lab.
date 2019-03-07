# ikiye ikilik listeyi önce ekrana bastır sonra matrisin determinantını bulunuz.

matris1=[[1,2],[3,4]]
matris2=[[1,2,3],[4,5,6],[7,8,9]]
matris3=[[3,6,30,5],[1,2,3,7],[4,5,6,7],[7,8,9,5]]

def det_from_2_by_2(m_1):
    s=m_1[0][0]*m_1[1][1]
    s2=m_1[0][1]*m_1[1][0]
    s3=s-s2
    return s3
print("matris 2x2:",matris1)
print ("matris 2x2 det:",det_from_2_by_2(matris1))
print("---------------------")

def delete_row_col_from_matrix(m_1,m,n):
    result=[]
    size_1=len(m_1)
    size_2=len(m_1[0])

    for i in range(size_1):
        if(i==m):
            continue
        row_1=[]
        for j in range(size_2):
            if(j==n):
                continue
            row_1.append(m_1[i][j])
        result.append(row_1)

    return result

def det_from_3_by_3(m_1):
    a_1=m_1[0][0]
    a_2=delete_row_col_from_matrix(matris2,0,0)
    a_3=det_from_2_by_2(a_2)
    a_4=a_1*a_3

    b_1=m_1[0][1]
    b_2 = delete_row_col_from_matrix(matris2, 0, 1)
    b_3 = det_from_2_by_2(b_2)
    b_4 = b_1 * b_3

    c_1=m_1[0][2]
    c_2 = delete_row_col_from_matrix(matris2, 0, 2)
    c_3 = det_from_2_by_2(c_2)
    c_4 = c_1 * c_3

    return a_4-b_4+c_4
print ("matris 3x3:",matris2)
print ("matris 3x3 det:",det_from_3_by_3(matris2))
print("---------------------")

def det_from_4_by_4(m_1):
    a_1=m_1[0][0]
    a_2=delete_row_col_from_matrix(m_1,0,0)
    a_3=det_from_3_by_3(a_2)
    a_4=a_1*a_3

    b_1=m_1[0][1]
    b_2 = delete_row_col_from_matrix(m_1, 0, 1)
    b_3 = det_from_3_by_3(b_2)
    b_4 = b_1 * b_3

    c_1=m_1[0][2]
    c_2 = delete_row_col_from_matrix(m_1, 0, 2)
    c_3 = det_from_3_by_3(c_2)
    c_4 = c_1 * c_3

    d_1 = m_1[0][3]
    d_2 = delete_row_col_from_matrix(m_1, 0, 3)
    d_3 = det_from_3_by_3(c_2)
    d_4 = d_1 * d_3


    return a_4-b_4+c_4-d_4

print("matris 4x4:",matris3)
print("matris 4x4 det:",det_from_4_by_4(matris3))
print("---------------------")

'''11 mart pazartesi ders saati baslangıcına aşagıdaki formatta çalışmalarınız teslim ediniz
            tarih  konu     github link   yükelenen tarih
                         screen capture githup                                                                                                                       '''