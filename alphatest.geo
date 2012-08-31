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
index: "av",
valid_begin: [0, 0],
valid_end: [0, 0],

mother: "world",

type: "sphere",
r_max: 6060.4,
r_min: 6000.0,
theta_delta: 20,

material: "acrylic_sno"
}
// {
// name: "GEO",
// index: "counter",
// valid_begin: [0, 0],
// valid_end: [0, 0],
// 
// mother: "av",
// 
// type: "sphere",
// r_max: 6005.3,
// theta_delta: 10,
// 
// material: "air"
// }
// // {
// name: "GEO",
// index: "gone",
// valid_begin: [0, 0],
// valid_end: [0, 0],
// 
// mother: "counter",
// 
// type: "polycone",
// Z: [0.0, 4242.6],
// Rout: [0.0, 6000.0],
// Rint: [0.0, 0.0],
// 
// material: "air",
// }
