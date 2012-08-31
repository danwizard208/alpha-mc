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
index: "counter_region", //Region in which events are generated
valid_begin: [0, 0],
valid_end: [0, 0],

mother: "world",

type: "sphere", //spherical section
r_max: 6000.0, //Outer radius
r_min: 5999.0, //Inner radius
theta_delta: 0.242593290202, //Maximum azimuth angle of counter

material: "acrylic_sno",
}
