
//내부모듈
import {postKdaNlpApi} from "../api"


const KdaList = () => {
    
    const onClick = e =>{
        e.preventDefault()
        postKdaNlpApi()
        .then((res)=>{
            console.log(`Response is ${res.config.data}`)
            localStorage.setItem('token', JSON.stringify(res.config.data))
            alert(`response : ${JSON.stringify(res.data.목록)}`)
            
        })
        .catch((err)=>{
            console.log(err)
            alert('다시 입력하세요.')
        })
    }

    return(
        <>
    <form method="POST">
        교전능력분석
        <button onClick={onClick} >
          입력 
        </button>
    </form>
        </>
    )
}

export default KdaList




