import re


text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Vestibulum dignissim feugiat nisl vel dapibus.
Donec eget felis velit.
Aenean diam neque, malesuada ut tristique non, pulvinar vitae augue.
Nullam rutrum varius nibh nec lacinia.
Aliquam odio nibh, tempus a erat id, auctor tempor tortor.
Mauris eu urna scelerisque ex convallis commodo vitae quis tellus.
Duis consequat magna quis congue rutrum.
Maecenas ornare, metus at aliquam suscipit, massa lectus pellentesque ligula, ac rutrum nulla urna quis purus...
Ut rutrum pharetra vestibulum!
Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos?
"""

sentences = text.split("\n")
# sentences = re.split("[\.\?\!]", text)
print(text)
# on_line_text = ("|".join(sentences))
on_line_text = text.replace("\n", " ")
print(sentences)
print(on_line_text)