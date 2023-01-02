//외부라이브러리
import { Container, Row, Col } from "react-bootstrap";
import { useState } from "react";
import { useSelector } from "react-redux";

//내부모듈
import { Detail } from "../";

//css
import "../css/Rayout.css";

const Rayout = () => {
  let [onOff, setOnOff] = useState(0);

  let state = useSelector((state) => state);

  return (
    <>
      <Container>
        {state.records.map((a, i) => (
          <Row className="rayout justify-content-md-center">
            <Col xs lg="2">
                
              {state.records[i].챔피언}
            </Col>
            <Col md="auto">{state.records[i].승패}</Col>
            <Col xs lg="2">
              {state.records[i].KDA}
            </Col>
            <Col>
              <botton
                style={{
                  backgroundColor: "orange",
                  width: "100px",
                  borderRadius: "10px",
                }}
                onClick={() => {
                  onOff === 0 ? setOnOff(1) : setOnOff(0);
                }}
              >
                상세보기
              </botton>
            </Col>
          </Row>
        ))}
        {onOff ? <Detail /> : null}
      </Container>
    </>
  );
};

export default Rayout;
