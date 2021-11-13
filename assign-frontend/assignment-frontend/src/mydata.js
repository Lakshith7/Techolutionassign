import React from 'react';
import axios from "axios";
import './mydata.css';

class mydata extends React.Component {
  
state={dat:[[]],a:false}
componentDidMount(){
    axios.get('http://127.0.0.1:8000/api/todos/')
    .then( response => {this.setState({dat:response.data,a:true})})
}
dget = (p) => {
  console.log(p);
  return p.map(ak=>(
    <td>{ak[0]+','+ak[1]}</td>
  ))
};
  render()
   {
    return (
      <div>
          {this.state.a?
          <table>
          <tr>
            <th>Category Name</th>
            <th> Category Colour</th>
            <th>Row and Coloumn points</th>
          </tr>
          {this.state.dat.map(d => (
            <tr>
              <td>{d[0]}</td>
              <td><svg width="50" height="20">
              <rect width="50" height="20" style={{ fill: `${d[1]}`}} />
              </svg></td>
              <td>{this.dget(d.slice(2))}</td>
              
            </tr>
            ))}
        </table>
          
          :""}
        </div>
      
      
    );
  }
}
export default mydata;

