"use client"

//login page
//will allow login and get token allong with redirect to correct directory

import axios from "axios";
import { Component, ReactNode } from "react";
import { GetGroup, checkToken, setToken } from "./serveractions";
import Navbar from "./common/navbar";

interface IState{
  username : string
  password : string
}

interface IProps{
  
}

class Page extends Component<IProps,IState> {
  constructor(props: IProps){
    super(props);
    this.state = {
      username : "",
      password : ""
    }
  }
  Auth = async() : Promise<void> => {
    console.log(this.state.username,this.state.password);
    await setToken(this.state.username,this.state.password);
    if(await checkToken()){
      var groups : string[] = await GetGroup();
      
    }
  }

  render(): ReactNode {
      return(
        <div className="w-full h-screen">
          <Navbar/>
          <div className=" max-w-96 m-auto flex-col border-2 rounded-md px-8 py-6">
            <div className=" flex gap-2 justify-center py-2">
              <label>Username </label>
              <input className="w-full border" value={this.state.username} onChange={(e)=>this.setState({username:e.target.value})}></input>
            </div>
            <div className=" flex gap-2 justify-center py-2">
              <label>Password </label>
              <input className="w-full border" value={this.state.password} onChange={(e)=>this.setState({password:e.target.value})}></input>
            </div>
            <div className="flex">
              <span className="grow"></span>
              <button className=" border rounded-md p-2 text-white bg-blue-500" onClick={()=>this.Auth()} >Log In</button>
            </div>
          </div>
        </div>
      )
  }
}

export default Page;