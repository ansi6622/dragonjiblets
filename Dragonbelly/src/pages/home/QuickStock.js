import React from 'react'

import { datas }from '../../data/default'

const QuickStockPage = () => (
      <div>
        <h2 className="phrases">Quick Stock</h2>
          <div className='col-xs-6'>
            <h3 className='text-center'>Stocks</h3>
            {datas.map((x, i) =>(
              <span
                key={i}
                className='btn quick-speech-button'>
                {x}
              </span>
            ))}
          </div>
        </div>
    );

export default QuickStockPage
