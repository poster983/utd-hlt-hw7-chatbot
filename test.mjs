//node ./test.mjs --experimental-json-modules
//
import { createRequire } from "module";
const require = createRequire(import.meta.url);
const kb = require("./knowledge_base.json")


console.log(Object.keys(kb).length)