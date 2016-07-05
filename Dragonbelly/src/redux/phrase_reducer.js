import {
  QUOTES,
} from './actions'

const INITIAL_STATE = { stocks: []};

export default function(state = INITIAL_STATE, action) {
  switch(action.type){

    case QUOTES:
      return { ...state,
        stocks: state.stocks.filter(x => (
          x.id !== action.payload.data.id[0]
        ))
      };

    default:
      return state
  }
}
