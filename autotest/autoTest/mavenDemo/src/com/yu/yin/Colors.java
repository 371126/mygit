package com.yu.yin;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import jxl.JXLException;
import jxl.Sheet;
import jxl.Workbook;
import jxl.read.biff.BiffException;
import net.sf.json.JSON;
import net.sf.json.JSONArray;
import net.sf.json.JSONObject;

public class Colors {
	public static void main(String[] args) throws IOException, JXLException {
		Workbook book = Workbook.getWorkbook(new File("/Users/yinyu/study/allTestVideo/数据同步表关系.xls"));
		Sheet sheet = book.getSheet(2);
		int rows = sheet.getRows();
		int cols = sheet.getColumns();
		List<JSON> js = new ArrayList<JSON>();
		String colname1 = sheet.getCell(0,0).getContents().trim();
		
		for(int i=1;i<rows;i++) {
			String name = sheet.getCell(0,i).getContents();
			if(!"[]".equals(name)) {
				list.add(name);
			}
		}
//		JSONObject jb = JSONObject.fromObject(list);
//		JSONArray ja = list.getJSONArray();
//		List<ColorData> colorList = new ArrayList<ColorData>();
//		for(int i=0;i<list.size();i++) {
//			ColorData cd = new ColorData();
//			cd.setColor(ja.getJSONArray(i).getString("color"));
//		}
		Map<String,String> map = new HashMap<String,String>();
		List<String> newList = new ArrayList<String>();
		String[] newStr = null;
		String[] newStr1 = null;
		for(int i=0;i<1;i++) {
			String value = list.get(i);
			for(int j=0;j<value.length();j++) {
				newStr = value.split(",");
//				value.replace(newValue, "");
//				System.out.println(value);
//				System.out.println(newValue);
			}
			
		}
		for (int i=0;i<1;i++) {
			newStr1 = newStr.toString().split("{");
//			System.out.println(newStr1);
		}
	}
	public static void getExcelData(File file) throws BiffException, IOException {
		Workbook book = Workbook.getWorkbook(file);			//获取文件信息
		Sheet sheet = book.getSheet(2);						//获取对应sheet页
		int rows = sheet.getRows();							//获取行数
		int cols = sheet.getColumns();						//获取列数
//		List<String> list = new ArrayList<String>();
		List<ColorData> list1 = new JSONArray();
		for(int i=1;i<rows;i++) {
			String name = sheet.getCell(0,i).getContents();
			if(!"[]".equals(name)) {
				list1=(List<ColorData>)JSONArray.toList(JSONArray.fromObject(name), ColorData.class);
				}
			for (ColorData stu : list1) {
				System.out.println(stu);
				}
			}
		ColorData[] ss =(ColorData[])JSONArray.toArray(JSONArray.fromObject(name),ColorData.class);
		for (ColorData student : ss) {
		System.out.println(student);
		}
	}
}
