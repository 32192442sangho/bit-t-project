import axios from 'axios'
const server = `http://localhost:8000`
export const postMinOutput = req => axios.post(`${server}/minoutput`, req)      