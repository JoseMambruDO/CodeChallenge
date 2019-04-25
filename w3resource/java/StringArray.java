import java.util.ArrayList;
import java.util.Arrays;

public class StringArray{


  public static void main(String... args){

    //This routine converts an ArrayList from String to an array of String
    ArrayList<String> arrayListString = new ArrayList<String> ();

    arrayListString.add("a");
    arrayListString.add("b");
    arrayListString.add("c");
    arrayListString.add("d");

    String[] arrayString =   Arrays.copyOf(arrayListString.toArray(),arrayListString.size(),String[].class);

    System.out.println(Arrays.toString( arrayString));
  }

}
