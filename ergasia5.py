def main():
      txt= input("Give me the file path: ")
      file=open (txt,"r+")
      words = file.read().split()
      newlist = []
      for word in words:
           newlist.append(Ay(word.strip()))
      result = ' '.join(newlist)
      print(result)
      file.seek(0)
      file.write(result)
      file.close



      def Ay(string):
           if len(string)>3:
              string = string[1:]+string[0:1]+"ay"
              return string
           else:
              return string


      main()             