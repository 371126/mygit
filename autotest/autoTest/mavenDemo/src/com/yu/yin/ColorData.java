package com.yu.yin;

public class ColorData {
	private String color;
	private String rgb;
	
	public String getColor() {
		return color;
	}
	public void setColor(String color) {
		this.color = color;
	}
	public String getRgb() {
		return rgb;
	}
	public void setRgb(String rgb) {
		this.rgb = rgb;
	}
	public ColorData(String color, String rgb) {
		this.color = color;
		this.rgb = rgb;
	}
	public ColorData() {	
	}
	
	@Override
	public String toString() {
		return "ColorData [color=" + color + ", rgb=" + rgb + "]";
	}
	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((color == null) ? 0 : color.hashCode());
		result = prime * result + ((rgb == null) ? 0 : rgb.hashCode());
		return result;
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		ColorData other = (ColorData) obj;
		if (color == null) {
			if (other.color != null)
				return false;
		} else if (!color.equals(other.color))
			return false;
		if (rgb == null) {
			if (other.rgb != null)
				return false;
		} else if (!rgb.equals(other.rgb))
			return false;
		return true;
	}
	
}
