import java.util.Arrays;
import java.util.List;

public class PathSplit{

  public static List splitPathStringToList(String path, String delim){
      return Arrays.asList( path.split(delim));
  }
  
  //This routine split a string by delimiter and print a array
  public static void main(String... arg){
      String delim = "\\\\";
      String path = "C:\\Example0\\Example1\\Example2\\Example3\\Example4\\Example5\\";
      System.out.println(splitPathStringToList(path, delim));
  }

}
