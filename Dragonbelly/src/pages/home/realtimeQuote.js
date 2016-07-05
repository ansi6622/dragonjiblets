import React from 'react'
import { getQuotes } from '../../redux/actions'
import ErrorBox from '../../components/ErrorBox'

const RealtimeQuotePage = () =>(

        <button className="btn btn-success" onClick={getQoutes()}>Log In</button>
    )



const mapStateToProps = (state) =>({
    user: state
});

export default RealtimeQuotePage;
