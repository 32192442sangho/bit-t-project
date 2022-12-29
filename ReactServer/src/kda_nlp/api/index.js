import axios from 'axios'
const server = `http://localhost:8000`
export const postKdaNlpApi = req => axios.post(`${server}/kdaNlp/kdaList`, req)      