const express = require('express') // 익스프레스 를 가져온다
const app = express()
const port = 5000



const mongoose = require("mongoose")
mongoose.connect('mongodb+srv://test_mongoDB:8VvoOwnW1pEDRuzW@myfirstcluster.gaapmdm.mongodb.net/?retryWrites=true&w=majority', {})
.then(() => console.log('MongoDB connected...'))
.catch(err => console.log(err))

app.get('/', (req, res) => res.send("HELLO WORDL!"))

app.listen(port, () => console.log(`example app listening on port ${port}!`))