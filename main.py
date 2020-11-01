from kivy.app import App
import math
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import numpy as np


def value(header, msg):
	pop = Popup(title=header,
	            content=Label(text=msg),
	            size_hint=(None, None), size=(400, 200))
	pop.open()


class MyGrid(Widget):
	pass


# Math equations
def side(aots, s1, s2):
	side = ((s1 ** 2) + (s2 ** 2) - 2 * s1 * s2 * math.cos(math.radians(aots)))
	return math.sqrt(round(side))


def cos(sota, s1, s2, letter):
	cos = ((s1 ** 2) + (s2 ** 2) - (sota ** 2)) / (2 * s1 * s2)
	answer_a = decdeg2dms(math.degrees(math.acos(cos)))
	return f"""{letter} = {answer_a}
{letter} in Decimal = {np.round(math.degrees(math.acos(cos)), 2)}
"""


def area_of_tri(side1, side2, inc_angle, label):
	sin_angle = math.sin(math.radians(inc_angle))
	area = (0.5 * side1 * side2) * sin_angle
	if label.text == "":
		label.text = f"""Area = {np.round(area, 2)}"""
	else:
		label.text = f"""{label.text}
Area = {np.round(area, 2)}
"""


def decdeg2dms(dd):
	is_positive = dd >= 0
	dd = abs(dd)
	minutes, seconds = divmod(dd * 3600, 60)
	degrees, minutes = divmod(minutes, 60)
	degrees = degrees if is_positive else -degrees
	return f"degrees = {degrees}     minutes = {minutes}    seconds = {np.round(seconds, 2)}"


def cos_fun(label, sota, s1, s2, letter):
	if sota.text and s1.text and s2.text != "":
		answer = cos(float(sota.text), float(s1.text), float(s2.text), letter)
		if label.text == "":
			label.text = f"""{answer}"""
		else:
			label.text = f"""{label.text}
{answer}
"""
	else:
		value("Missing Values", "Please Enter All 3 Sides")


def side_fun(label, aots, s1, s2, letter):
	if aots.text and s1.text and s2.text != "":
		answer = side(float(aots.text), float(s1.text), float(s2.text))
		if label.text == "":
			label.text = f"""Side {letter} = {np.round(answer)}"""
		else:
			label.text = f"""{label.text}
Side {letter} = {np.round(answer)}
"""
	else:
		value("Missing Values", "One or more required value is missing")


# logic
class MyApp(App):

	# functions
	def clear_output(self):
		label = self.root.ids.label
		label.text = ""

	def reset_all(self):
		label = self.root.ids.label
		input_side_a = self.root.ids.box_a
		input_side_b = self.root.ids.box_b
		input_side_c = self.root.ids.box_c
		input_angle_a = self.root.ids.box_angle_a
		input_angle_b = self.root.ids.box_angle_b
		input_angle_c = self.root.ids.box_angle_c
		label.text = ""
		input_angle_a.text = ""
		input_angle_b.text = ""
		input_angle_c.text = ""
		input_side_a.text = ""
		input_side_b.text = ""
		input_side_c.text = ""

	# angle finders
	def calc_a(self):
		label = self.root.ids.label
		sota = self.root.ids.box_a
		s1 = self.root.ids.box_b
		s2 = self.root.ids.box_c
		cos_fun(label, sota, s1, s2, letter="A")

	def calc_b(self):
		label = self.root.ids.label
		sota = self.root.ids.box_b
		s1 = self.root.ids.box_a
		s2 = self.root.ids.box_c
		cos_fun(label, sota, s1, s2, letter="B")

	def calc_c(self):
		label = self.root.ids.label
		sota = self.root.ids.box_c
		s1 = self.root.ids.box_a
		s2 = self.root.ids.box_b
		cos_fun(label, sota, s1, s2, letter="C")

	# side finders
	def side_a(self):
		label = self.root.ids.label
		aots = self.root.ids.box_angle_a
		s1 = self.root.ids.box_b
		s2 = self.root.ids.box_c
		side_fun(label, aots, s1, s2, letter="A")

	def side_b(self):
		label = self.root.ids.label
		aota = self.root.ids.box_angle_b
		s1 = self.root.ids.box_a
		s2 = self.root.ids.box_c
		side_fun(label, aota, s1, s2, letter="B")

	def side_c(self):
		label = self.root.ids.label
		aota = self.root.ids.box_angle_c
		s1 = self.root.ids.box_b
		s2 = self.root.ids.box_a
		side_fun(label, aota, s1, s2, letter="C")


#Area
	def area(self):
		label = self.root.ids.label
		side_a = self.root.ids.box_a
		side_b = self.root.ids.box_b
		side_c = self.root.ids.box_c
		angle_a = self.root.ids.box_angle_a
		angle_b = self.root.ids.box_angle_b
		angle_c = self.root.ids.box_angle_c

		if angle_a.text and side_b.text and side_c.text != "":
			angle_a = float(angle_a.text)
			side_b = float(side_b.text)
			side_c = float(side_c.text)
			area_of_tri(side1=side_b, side2=side_c, inc_angle=angle_a, label=label)

		elif angle_b.text and side_a.text and side_c.text != "":
			angle_b = float(angle_b.text)
			side_a = float(side_a.text)
			side_c = float(side_c.text)
			area_of_tri(side1=side_a, side2=side_c, inc_angle=angle_b, label=label)

		elif angle_c.text and side_a.text and side_b.text != "":
			angle_c = float(angle_a.text)
			side_b = float(side_b.text)
			side_a = float(side_c.text)
			area_of_tri(side1=side_a, side2=side_b, inc_angle=angle_c, label=label)
		else:
			value("Missing Values", "Please enter 2 side and their included angle")

	def build(self):
		return MyGrid()


if __name__ == "__main__":
	MyApp().run()
