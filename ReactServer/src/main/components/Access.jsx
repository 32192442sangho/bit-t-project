//외부라이브러리
import {useNavigate} from "react-router-dom";
import {useState} from 'react'

//내부모듈
import {postMainApi} from "../api"

//css
import "../css/input.css";

const Access = () => {
  let navigate = useNavigate();
  const [inputs, setInputs] = useState({})
  const {Name} = inputs;
  
  const onChange = e => {
      e.preventDefault()
      const {value, name} = e.target 
      setInputs({...inputs, [name]: value})
  }

  const onClick = e =>{
    e.preventDefault()
    const nameRequests = {Name}
    alert(`사용자 이름: ${JSON.stringify(nameRequests)}`)
    postMainApi(nameRequests)
    .then((res)=>{
        navigate("/records");
        console.log(`Response is ${res.config.data}`)
        localStorage.setItem('token', JSON.stringify(res.config.data))
        alert(`닉네임 : ${JSON.stringify(res.data.name)}`)    
    })
    .catch((err)=>{
        console.log(err)
        alert('다시 입력하세요.')
    })
}

  return(
    <>
    <form method="POST">
      아이디 : <input type="text" name="Name" onChange={onChange} /><br/>
        <button onClick={onClick} >
          입력 
        </button>
    </form>
    </>
  )
};



export default Access;
