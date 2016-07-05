import { combineReducers } from 'redux'

import PhraseReducer from './phrase_reducer'

export default combineReducers({
  stocks: PhraseReducer
});
