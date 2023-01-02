// css
import "../css/background.css";
import { Container, Row, Col } from "react-bootstrap";

const Background = () => {
  return (
    <>
      <div className="summoner">
        <div className="info"></div>
        <Container>
          <Row>
            <Col>소환사이름</Col>
            <Col>티어</Col>
            <h1>{localStorage.getItem("user")}</h1>
          </Row>
        </Container>
      </div>
    </>
  );
};

export default Background;
