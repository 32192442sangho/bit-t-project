import axios from 'axios'
const server = `http://localhost:8000`
export const postAshOutput = req => axios.post(`${server}/ashoutput`, req)      