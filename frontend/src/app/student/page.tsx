"use client"

import axios from "axios";
import { Component, ReactNode } from "react";
import Navbar from "../common/navbar";

interface IState{
  details:any
}

interface IProps{
  
}

class Page extends Component<IProps,IState> {
  constructor(props: IProps){
    super(props);
    this.state = {
      details : null
    }
  }
  componentDidMount(): void {
      axios.get("http://localhost:8000").then((res)=>{
        res.data.map((id:number,output:any)=>console.log(id,output.firstname,output.lastname))
        this.setState({details:res.data});
      }).catch(err=>{})
  }

  add(fname :string,lname:string) {
    axios.post("http://localhost:8000",{
      firstname : fname,
      lastname : lname
    }).then(response=>
      console.log(response)
    ).catch(err=>{})
  }
  render(): ReactNode {
      return(
        <>
        <Navbar/>
          <div className="flex gap-2">
            {this.state.details==null?null:this.state.details.map((output:any)=>(
              <div id={`${output.firstname+output.lastname}`} className="border rounded-md p-2">
                <h1>{output.firstname}</h1>
                <h1>{output.lastname}</h1>
              </div>
            ))}
          </div>
        </>
      )
  }
}

export default Page;