import axios from 'axios'
export const QUOTES = 'QUOTES';
const API = 'http://localhost:3000'

export function getQuotes(id){
  const request = axios.get(`${API}/hello`);
  return{
    type: QUOTES,
    payload: request
  }
}
