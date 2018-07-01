package com.yu.yin;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

import jxl.Sheet;
import jxl.Workbook;
import jxl.read.biff.BiffException;
import jxl.write.Label;
import jxl.write.WritableSheet;
import jxl.write.WritableWorkbook;
import jxl.write.WriteException;
import jxl.write.biff.RowsExceededException;
import net.sf.json.JSONArray;

public class NewColor {
	public static void main(String[] args) throws BiffException, IOException, RowsExceededException, WriteException {
		File file = new File("/Users/yinyu/study/allTestVideo/数据同步表关系.xls");
		Workbook book = Workbook.getWorkbook(file);
		Sheet sheet = book.getSheet(2);
		int rows = sheet.getRows();
		int cols = sheet.getColumns();
		List<ColorData> list1 = new JSONArray();
		HashSet<ColorData> hs = new HashSet<ColorData>();
		for(int i=0;i<rows;i++) {
			String name = sheet.getCell(0,i).getContents();
			if(!"[]".equals(name)) {
				list1=(List<ColorData>)JSONArray.toList(JSONArray.fromObject(name), ColorData.class);
				hs.addAll(list1);
			}
		}
		List<String> colors = new ArrayList<String>();
		List<String> rgb = new ArrayList<String>();
		for (ColorData colorData : hs) {
//			System.out.println("color:"+colorData.getColor()+"...rgb:"+colorData.getRgb());
			colors.add(colorData.getColor());
			rgb.add(colorData.getRgb());
		}
		System.out.println(hs.size());
		WritableWorkbook wb = Workbook.createWorkbook(new File("/Users/yinyu/study/allTestVideo/newcolor.xls"));
		WritableSheet colorSheet = wb.createSheet("color", 0);
		Label label1 = new Label(0, 0, "color");
		Label label2 = new Label(1, 0, "rbg");
		colorSheet.addCell(label1);
		colorSheet.addCell(label2);
		for(int i=1;i<hs.size();i++) {
			Label label = new Label(0, i, colors.get(i-1));
			Label labell = new Label(1, i, rgb.get(i-1));
			colorSheet.addCell(label);
			colorSheet.addCell(labell);
		}
		wb.write();
		wb.close();
	}
}
