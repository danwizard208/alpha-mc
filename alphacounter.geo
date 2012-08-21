{
name: "GEO",
index: "world",
valid_begin: [0, 0],
valid_end: [0, 0],
invisible: 1,

mother: "",

type: "box",
size: [10000.0, 10000.0, 10000.0],

material: "rock"
}

{
name: "GEO",
index: "counter_region",
valid_begin: [0, 0],
valid_end: [0, 0],

mother: "world",

type: "sphere",
r_max: 6000.0,
r_min: 5999.0,
theta_delta: 0.242593290202,

material: "acrylic_sno",
}
