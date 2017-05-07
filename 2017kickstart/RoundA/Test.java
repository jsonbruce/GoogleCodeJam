package leetcode;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Test {

	public static long getNum(int r, int c){
//		int r = 1000;
//		int c = 500;
		int min = Math.min(r, c);
		long num = 0;
		for(int i = 1; i < min; i++){
			num += (r-i)*(c-i)*i;
			
		}
		return num % 1000000007;
//		System.out.println(num % 1000000007);
		
	}
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		String outFileName = "result.tab";
		FileWriter fileWriter = new FileWriter(outFileName);
		String fileName = "A-small-attempt5.in";
		String line = "";
		BufferedReader in = new BufferedReader(new FileReader(fileName));
		line = in.readLine();
		int t = Integer.parseInt(line);
		for(int i = 0; i < t; i++){
			line = in.readLine();
			int r = Integer.parseInt(line.split(" ")[0]);
			int c = Integer.parseInt(line.split(" ")[1]);
			long num = getNum(r,c);
//			System.out.println(num);
			String outline = "Case #" + (i+1) +": " + num + "\n";
			System.out.print(outline);
			fileWriter.write(outline);			
		}
		fileWriter.close();


	}

}
