tam = ('\n')  #換行
again='Y'
print('This advanced code is based on website-')
print('https://www.jb51.net/article/238054.htm')
print(tam*3)  #換行

while again=='Y'or'y':
  again='N'
  print(tam) 

#loop for alt lines
  convo_list_1 = ['Hi, Welcome to use cipher-text translational system--V.3.0.', 'This dictionary can translat between eng and encrpition code', 'Which dictionary you want to use??']
  for each_convo in convo_list_1:
    print(each_convo)
    print(tam)  #換行
#-----------------------------
#Chose the dictionary

  print(tam)  #換行

  print('1.Morse Code')
  print('2.Caesar Code')
  print('3.ASCII')
  print(tam)  #換行
  
  dictionary_choice = input()
  dictionary_choice = int(dictionary_choice)
  
  if    dictionary_choice ==1 :
      #-----------------------------
      #  morse code
      #This improved code is based https://www.jb51.net/article/238054.htm
      
      
      
      tam = ('\n')  #換行
      
      #-----------------------------
      
      
      
      diction_A = {
              'A': '.-',
              'B': '-...',
              'C': '-.-.',
              'D': '-..',
              'E': '.',
              'F': '..-.',
              'G': '--.',
              'H': '....',
              'I': '..',
              'J': '.---',
              'K': '-.-',
              'L': '.-..',
              'M': '--',
              'N': '-.',
              'O': '---',
              'P': '.--.',
              'Q': '--.-',
              'R': '.-.',
              'S': '...',
              'T': '-',
              'U': '..-',
              'V': '...-',
              'W': '.--',
              'X': '-..-',
              'Y': '-.--',
              'Z': '--..',
              '1': '.----',
              '2': '..---',
              '3': '...--',
              '4': '....-',
              '5': '.....',
              '6': '-....',
              '7': '--...',
              '8': '---..',
              '9': '----.',
              '0': '-----',
              ', ': '--..--',
              '.': '.-.-.-',
              '?': '..--..',
              '/': '-..-.',
              '-': '-....-',
              '(': '-.--.',
              ')': '-.--.-'
          }
      
      # 表示摩斯密码图的字典
      #return
      print(tam)
      
      
      # 根据摩斯密码图对字符串进行加密的函数
      # ues[ for  n.n in  mess.age to let(A='abc') ---) a,b,c ]
      def be_code(mm):
          cipher = ''
          for nn in mm:
              if nn != ' ':
                  # 查字典并添加对应的摩斯密码
                  # 用空格分隔不同字符的摩斯密码
                  cipher += diction_A[nn] + ' '
              else:
                  # 1个空格表示不同的字符
                  # 2表示不同的词
                  cipher += ' '
          return cipher
      
            
      
      
      # 将字符串从摩斯解密为英文的函数
      def Be_text(mm):
          # 在末尾添加额外空间以访问最后一个摩斯密码
          mm += ' '
          decipher = ''
          citext = ''
          global i
          for nn in mm:
              # 检查空间
              if nn != ' ':
                  i = 0
                  # 在空格的情况下
                  citext += nn
              # 在空间的情况下
              else:
                  # 如果 i = 1 表示一个新字符
                  i += 1
                  # 如果 i = 2 表示一个新单词
                  if i == 2:
                      # 添加空格来分隔单词
                      decipher += ' '
                  else:
                      # 使用它们的值访问密钥（加密的反向）
                      decipher += list(diction_A.keys())[list(
                          diction_A.values()).index(citext)]
                      citext = ''
          return decipher
      
      
      print('Which way you want use??')
      print(tam)  #換行
      print('1.original-text to cipher-text')
      print('2.cipher-text to original-text')
      print(tam)  #換行
      way_choice = input()
      print(tam)  #換行
      print('What text you want to translate with?')
      message_1 = input()
      
      tam = ('\n')  #換行
      print(tam)  #換行
      
      way_choice = int(way_choice)
      if way_choice == 1 :
      
          def main():  #準備 被翻譯成密文 的 明文
      
              #result = be_code(message_1.upper())
              #print(result)
              print('That cipher-text is...')
              print(be_code(message_1.upper()))
      elif way_choice == 2 :
      
          def main():
      
              #準備 被翻譯成明文 的 密文
      
              #result = Be_text(message_2)
              #print(result)
              print('The original-test is...')
              print(Be_text(message_1))
            
      
      # 執行主函数
      #----------------------------
      
      
      main()
      print(tam)    
      print('Again?')
      print('Y.Yes')
      print('N.No')
      again=input()
      #morse code
      #-----------------------------
      
  if    dictionary_choice ==2 :
    print('Which way you want use??')
    print(tam)  #換行
    print('1.original-text to cipher-text')
    print('2.cipher-text to original-text')
    print(tam)  #換行
    way_choice = input()
    #way_choice=2
    way_choice=int(way_choice)
    
    print('What is your key?')
    n=input()
    n=int(n)
    
    if way_choice ==1:
        n=(n)
    elif way_choice ==2:
        n=(-n)
        
        
    
    n=int(n)    
    #print(n)
         
    
      
  
    
    print('What text you want to translate with?')
    M=input()
    
    str(M)
    M=M.upper()
    #print(M)
    
    
    diction_A = {
            'A': 1+n,
            'B': 2+n,
            'C': 3+n,
            'D': 4+n,
            'E': 5+n,
            'F': 6+n,
            'G': 7+n,
            'H': 8+n,
            'I': 9+n,
            'J': 10+n,
            'K': 11+n,
            'L': 12+n,
            'M': 13+n,
            'N': 14+n,
            'O': 15+n,
            'P': 16+n,
            'Q': 17+n,
            'R': 18+n,
            'S': 19+n,
            'T': 20+n,
            'U': 21+n,
            'V': 22+n,
            'W': 23+n,
            'X': 24+n,
            'Y': 25+n,
            'Z': 26+n,
            ' ': 9999,
        }
    
    mm=""
    for nn in M:
        w_r_A=diction_A[nn]
        
        
        w_r_A=str(w_r_A)
        
        
        mm=mm+w_r_A+','
    
    #print(mm)
    mm=mm[0:-1]
    #print(mm)
    #.................................................
    #making diction_B
    
    A_123=-25
    A_123_N=''
    while A_123<53:
        A_123=str(A_123)
        A_123_N=A_123_N+A_123+','
        A_123=int(A_123)
        A_123=A_123+1
        
    
    A_123_N=A_123_N[0:-1]
    #print(A_123_N)
    A_123_N=A_123_N+','+"9999"
    #print(A_123_N)
    
    
    A_123_N=A_123_N.split(',')
    
    
    
    #https://www.delftstack.com/zh-tw/howto/python/python-convert-list-of-strings-to-ints/
    A_123_N = list(map(int, A_123_N))
    #print(A_123_N)
    
    
    A_ABC='A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z, '
    A_ABC=A_ABC.split(',')
    
    
    
    
    diction_B=dict(zip(A_123_N,A_ABC))
    
    
    #.................................................
    
    
    
    xx=mm.split(',')
    #print(xx)
    #print(type(xx))
    #Fincal_ans=''
    final_ans_texs=''
    for nn_B in xx:
      nn_B=int(nn_B)
      w_r_B=diction_B[nn_B]
      final_ans_texs=final_ans_texs+w_r_B
      
      
        #w_r_B=diction_B[nn_B]
        
        
        
    
    
    final_ans_texs=final_ans_texs.lower()
    print(final_ans_texs)
    print(tam) 
    print('Again?')
    print('Y.Yes')
    print('N.No')
    again=input()
  
  
  if    dictionary_choice ==3 :
    def remind():
      print('Ok, please type your input by list.')
      print('For example, if you choice')
      print(' (dec 十進制)(bin 二進制) (hix十六進制)')
      print('Pease type by list, like 97,98,99 ')
      print('or 1100001,1100010,1100011 ')
      print('or 5E,4C,3F')
      print(tam)  #換行
      print('But if your input is text, ignore this remind :)')
      
    print('Which type is your input source??')
    print(tam)  #換行
    
    print('1.ENG-text')
    print('2.dec')
    print('3.bin')
    print('4.hex')
    input_source=input()
    input_source=int(input_source)
    print(tam)  #換行
    print('Which type is your output source??')
    print(tam)  #換行
    print('1.ENG-text')
    print('2.dec')
    print('3.bin')
    print('4.hex')
    output_source=input()
    output_source=int(output_source)
    print(tam)#換行
    remind()
    print(tam)#換行
    print('What is your text?')
    INPUT=input()
    
    #print(INPUT)
    # INPUT will be def first.
    def text_to_dec():
      OUTPUT=''
      global INPUT
      for tmp in INPUT:
        
        tmp=ord(tmp)
        #print(n)
        tmp=str(tmp)
        OUTPUT=OUTPUT+tmp+','
      OUTPUT=OUTPUT[0:-1]
      #print(OUTPUT)
      return OUTPUT
      
    def dec_to_text():
      global INPUT
      #在函數外 定義的值     
      #函數內不知道
      #需要聲明一次（global）,
      #同理,函數內運算完的值
      #函數外 也不能調用
      #需要向外發送一次（return)
      
      
      INPUT=INPUT.split(',')
      OUTPUT=''
      for tmp in INPUT:
        tmp=int(tmp)
        tmp=chr(tmp)
        OUTPUT=OUTPUT+tmp
      return OUTPUT
    
    def dec_to_bin():
      global INPUT
      INPUT=INPUT.split(',')
      OUTPUT=""
      for tmp in INPUT:
        #print(tmp)
        tmp=int(tmp)
        tmp=bin(tmp)
        tmp=str(tmp)
        tmp=tmp[2:20]
        OUTPUT=OUTPUT+tmp+','
        
      OUTPUT=OUTPUT[0:-1]  
      return OUTPUT  
    def dec_to_hex():
      global INPUT
      INPUT=INPUT.split(',')
      OUTPUT=""
      for tmp in INPUT:
        #print(tmp)
        tmp=int(tmp)
        tmp=hex(tmp)
        tmp=str(tmp)
        tmp=tmp[2:20]
        OUTPUT=OUTPUT+tmp+','
        
      OUTPUT=OUTPUT[0:-1]  
      return OUTPUT    
    def bin_to_dec():
      global INPUT
      INPUT=INPUT.split(',')
      OUTPUT=''
      for tmp in INPUT:
        
        tmp=int(tmp,2)
        tmp=str(tmp)
        
        OUTPUT=OUTPUT+tmp+','
      OUTPUT=OUTPUT[0:-1]  
      return OUTPUT  
    
    def hex_to_dec():
      global INPUT
      INPUT=INPUT.split(',')
      OUTPUT=''
      for tmp in INPUT:
        
        tmp=int(tmp,16)
        tmp=str(tmp)
        
        OUTPUT=OUTPUT+tmp+','
      OUTPUT=OUTPUT[0:-1]  
      return OUTPUT  
    
    if input_source==1:
      if output_source ==1:
        print(INPUT)
        
      if  output_source ==2:
        OUTPUT=text_to_dec()
        print(OUTPUT)
        
      if  output_source ==3:
        OUTPUT=text_to_dec()
        #print(OUTPUT)
        #print(type(OUTPUT))
        INPUT=OUTPUT
        
        OUTPUT=dec_to_bin()
        print(OUTPUT)
        
      if  output_source ==4:
        OUTPUT=text_to_dec()
        INPUT=OUTPUT
        OUTPUT=dec_to_hex()
        print(OUTPUT)
      
    
    if input_source==2:
      
      if output_source ==1:
        #OUTPUT=INPUT
        #dec_to_text()
        OUTPUT=dec_to_text()
        print(OUTPUT)
      if output_source ==2:
        print(INPUT)
      if output_source ==3:
        OUTPUT=dec_to_bin()
        print(OUTPUT)
      if output_source ==4:
        OUTPUT=dec_to_hex()
        print(OUTPUT)
    
    if input_source==3:
      if output_source ==1:
        OUTPUT=bin_to_dec()
        INPUT=OUTPUT
        OUTPUT=dec_to_text()
        print(OUTPUT)
      if output_source ==2:
        OUTPUT=bin_to_dec()
        print(OUTPUT)
      if output_source ==3:
        OUTPUT=INPUT
        print(OUTPUT)
      if output_source ==4:
        OUTPUT=bin_to_dec()
        INPUT=OUTPUT
        OUTPUT=dec_to_hex()
        print(OUTPUT)
        
        
    
    if input_source==4:
      if output_source ==1:
        OUTPUT=hex_to_dec()
        INPUT=OUTPUT
        OUTPUT=dec_to_text()
        print(OUTPUT)
      if output_source ==2:
        OUTPUT=hex_to_dec()
        print(OUTPUT)
      if output_source ==3:
        OUTPUT=hex_to_dec()
        INPUT=OUTPUT
        OUTPUT=dec_to_bin()
        print(OUTPUT)
      if output_source ==4:
        OUTPUT=INPUT
        print(OUTPUT)

    print(tam)     
    print('Again?')
    print('Y.Yes')
    print('N.No')
    again=input() 

  print(tam)  #換行
