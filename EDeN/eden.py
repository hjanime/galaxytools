"""
EDeN filetypes
"""

from galaxy.datatypes.data import Binary


class Gspan( Binary ):
    """Class describing an gSpan file"""
    file_ext = "gspan"

    def set_peek( self, dataset, is_multi_byte=False ):
        if not dataset.dataset.purged:
            dataset.peek  = "gSpan" 
            dataset.blurb = data.nice_size( dataset.get_size() )
        else:
            dataset.peek = 'file does not exist'
            dataset.blurb = 'file purged from disk'
    def display_peek( self, dataset ):
        try:
            return dataset.peek
        except:
            return "Binary gSpan file (%s)" % ( data.nice_size( dataset.get_size() ) )

class SparseVector( Binary ):
    """Class describing an SparseVector file"""
    file_ext = "sparse"

    def set_peek( self, dataset, is_multi_byte=False ):
        if not dataset.dataset.purged:
            dataset.peek  = "SparseVector" 
            dataset.blurb = data.nice_size( dataset.get_size() )
        else:
            dataset.peek = 'file does not exist'
            dataset.blurb = 'file purged from disk'
    def display_peek( self, dataset ):
        try:
            return dataset.peek
        except:
            return "Binary SparseVector file (%s)" % ( data.nice_size( dataset.get_size() ) )
