from kivy.app import App
import math
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


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
{letter} in Decimal = {math.degrees(math.acos(cos))} 
"""


def decdeg2dms(dd):
	is_positive = dd >= 0
	dd = abs(dd)
	minutes, seconds = divmod(dd * 3600, 60)
	degrees, minutes = divmod(minutes, 60)
	degrees = degrees if is_positive else -degrees
	return f" degrees = {degrees}     minutes = {minutes}    seconds = {seconds}"


def cos_fun(label, sota, s1, s2, letter):
	ans = cos(float(sota.text), float(s1.text), float(s2.text), letter)
	label.text = f""" {label.text} 
 {ans}"""


def side_fun(label, aots, s1, s2, ):
	ans = side(float(aots.text), float(s1.text), float(s2.text))
	label.text = f""" {label.text} 
 {round(ans)}"""


# logic
class MyApp(App):

	# angle finders
	def calc_a(self):
		label = self.root.ids.label
		sota = self.root.ids.box_a
		s1 = self.root.ids.box_b
		s2 = self.root.ids.box_c
		letter = "A"
		cos_fun(label, sota, s1, s2, letter)

	def calc_b(self):
		label = self.root.ids.label
		sota = self.root.ids.box_b
		s1 = self.root.ids.box_a
		s2 = self.root.ids.box_c
		letter = "B"
		cos_fun(label, sota, s1, s2, letter)

	def calc_c(self):
		label = self.root.ids.label
		sota = self.root.ids.box_c
		s1 = self.root.ids.box_a
		s2 = self.root.ids.box_b
		letter = "C"
		cos_fun(label, sota, s1, s2, letter)

	# side finders
	def side_a(self):
		label = self.root.ids.label
		aots = self.root.ids.box_angle_a
		s1 = self.root.ids.box_b
		s2 = self.root.ids.box_c
		side_fun(label, aots, s1, s2)

	def side_b(self):
		label = self.root.ids.label
		aota = self.root.ids.box_angle_b
		s1 = self.root.ids.box_a
		s2 = self.root.ids.box_c
		side_fun(label, aota, s1, s2)

	def side_c(self):
		label = self.root.ids.label
		aota = self.root.ids.box_angle_c
		s1 = self.root.ids.box_b
		s2 = self.root.ids.box_a
		side_fun(label, aota, s1, s2)

	def build(self):
		return MyGrid()


if __name__ == "__main__":
	MyApp().run()
