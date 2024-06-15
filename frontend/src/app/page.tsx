"use client"

//login page
//will allow login and get token allong with redirect to correct directory

import { Component, ReactNode } from "react";
import { GetGroup, checkToken, setToken } from "./serveractions";
import { AcademicCapIcon } from "@heroicons/react/24/outline";
import { cookies } from "next/headers";
import { subtle } from "crypto";

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
      cookies().set("",subtle.encrypt(subtle.aes,(JSON.stringify(groups))));
      console.log(groups);
    }
  }

  render(): ReactNode {
      return(
        <div className="w-full h-screen">
          <div className=" h-16 flex items-center gap-2 mx-8 my-6"><AcademicCapIcon className="h-full"/><span className="text-4xl">OnMark</span></div>
          <div className=" h-5/6 content-center">
            <div className=" sm:max-w-96 max-w-72 mx-auto px-8 py-6 shadow-xl rounded-2xl border-t border-gray-500">
              <h1 className=" text-4xl mb-4">Log In</h1>
              <div className="form-control mb-4">
                <input placeholder="Username" type="text" className="input input-bordered" value={this.state.username} onChange={(e)=>this.setState({username:e.target.value})}></input>
              </div>
              <div className="form-control mb-4">
                <input className="input input-bordered" placeholder="Password" type="password" value={this.state.password} onChange={(e)=>this.setState({password:e.target.value})}></input>
              </div>
              <div className="form-control">
                <button className="btn btn-accent" onClick={()=>this.Auth()} >Log In</button>
              </div>
            </div>
          </div>
        </div>
      )
  }
}

export default Page;