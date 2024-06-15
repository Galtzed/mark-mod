import { ReactNode } from "react";

export default function() : ReactNode{
    return(
        <div className="w-full flex border-b-2 p-2 mb-2 gap-2">
            <a href="/about" className="text-2xl"> OnMark</a>
            <span className="grow"></span>
        </div>
    )
}