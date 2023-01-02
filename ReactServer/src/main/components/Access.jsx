//외부라이브러리
import { useNavigate } from "react-router-dom";
import { useState } from "react";
import { InputGroup, Form, Button } from "react-bootstrap";

//내부모듈
import { postMainApi } from "../api";

//css
import "../css/input.css";

const Access = () => {
  let navigate = useNavigate();

  const [inputs, setInputs] = useState({});
  const { Name } = inputs;

  const onChange = (e) => {
    e.preventDefault();
    const { value, name } = e.target;
    setInputs({ ...inputs, [name]: value });
    console.log(inputs[""]);
  };

  const onClick = (e) => {
    e.preventDefault();
    const nameRequests = { Name };
    alert(`사용자 이름: ${JSON.stringify(nameRequests)}`);
    postMainApi(nameRequests)
      .then((res) => {
        console.log(`Response is ${res.config.data}`);
        localStorage.setItem("token", JSON.stringify(res.config.data));
        alert(`닉네임 : ${JSON.stringify(res.data.name)}`);
      })
      .catch((err) => {
        console.log(err);
        alert("다시 입력하세요.");
      });
    localStorage.setItem("user", inputs[""]);
    navigate(`/records/${localStorage.getItem("user")}`);
  };

  return (
    <>
      <div className="input">
        <InputGroup className="mb-3">
          <Form.Control
            placeholder="소환사 이름"
            aria-label="Recipient's username"
            aria-describedby="basic-addon2"
            onChange={onChange}
          />
          <Button
            onClick={onClick}
            variant="outline-secondary"
            id="button-addon2"
          >
            Button
          </Button>
        </InputGroup>
      </div>
    </>
  );
};

export default Access;
